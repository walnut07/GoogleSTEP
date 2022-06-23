//
// >>>> malloc challenge! <<<<
//
// Your task is to improve utilization and speed of the following malloc
// implementation.
// Initial implementation is the same as the one implemented in simple_malloc.c.
// For the detailed explanation, please refer to simple_malloc.c.

#include <assert.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//
// Interfaces to get memory pages from OS
//

void *mmap_from_system(size_t size);
void munmap_to_system(void *ptr, size_t size);

//
// Struct definitions
//

typedef struct my_metadata_t {
  size_t size;
  struct my_metadata_t *next;
} my_metadata_t;

typedef struct my_heap_t {
  my_metadata_t *free_head;
  my_metadata_t dummy;
} my_heap_t;

//
// Static variables (DO NOT ADD ANOTHER STATIC VARIABLES!)
//
int num_of_bin = 7;
my_heap_t bins[7];

int get_my_bin(size_t size) {
  for (int i = 0; i < num_of_bin; i++) {
    if (i * 1000 <= size && size < (i + 1) * 1000) {
      return i;
    }
  }
}

//
// Helper functions (feel free to add/remove/edit!)
//

my_heap_t  my_add_to_free_list(my_metadata_t *metadata, int my_bin_idx) {
  assert(!metadata->next);
  metadata->next = bins[my_bin_idx].free_head;
  bins[get_my_bin(metadata->size)].free_head = metadata; 
  
}

void my_remove_from_free_list(my_metadata_t *metadata, my_metadata_t *prev, int remove_bin_idx) {
  if (prev) {
    prev->next = metadata->next;
  } else {
    bins[remove_bin_idx].free_head = metadata->next;
  }
  metadata->next = NULL;
}

//
// Interfaces of malloc (DO NOT RENAME FOLLOWING FUNCTIONS!)
//

// This is called at the beginning of each challenge.
void my_initialize() {
  for(int i = 0; i < num_of_bin; i++){
    bins[i].free_head = &bins[i].dummy;
    bins[i].dummy.size = 0;
    bins[i].dummy.next = NULL;
  }
}

// my_malloc() is called every time an object is allocated.
// |size| is guaranteed to be a multiple of 8 bytes and meets 8 <= |size| <=
// 4000. You are not allowed to use any library functions other than
// mmap_from_system() / munmap_to_system().
void *my_malloc(size_t size) {
  int my_bin_idx = get_my_bin(size);
  my_metadata_t *metadata = bins[my_bin_idx].free_head;
  my_metadata_t *prev = NULL;
  my_metadata_t *min_free = NULL; // A pointer that points to the smallest metadata among the ones whose size is bigger than the argument `size`. 引数のsizeより大きいサイズを持つfree_headの中で、サイズがもっとも小さいものを指すポインタ。
  my_metadata_t *min_free_prev = NULL;

  while (!min_free && my_bin_idx < num_of_bin) {
    my_metadata_t *metadata = bins[my_bin_idx].free_head;
    my_metadata_t *prev = NULL;
    while (metadata) {
      if (metadata->size >= size) { // metadata has enough space if it's size is bigger than `size`.
        if (!min_free) {
          min_free = metadata; 
          min_free_prev = prev;
        }
        else if (min_free->size > metadata->size) {
          min_free = metadata; 
          min_free_prev = prev;
        }
      }
      prev = metadata;
      metadata = metadata->next;
    }
    my_bin_idx++;
  }

  metadata = min_free; 
  prev = min_free_prev;
  // now, metadata points to the free_head whose size is bigger than `size` and smallest among them.
  // and prev is the entry previous to metadata.

  if (!metadata) {
    // There was no free slot available. We need to request a new memory region
    // from the system by calling mmap_from_system().
    //
    //     | metadata | free slot |
    //     ^
    //     metadata
    //     <---------------------->
    //            buffer_size
    size_t buffer_size = 4096;
    my_metadata_t *metadata = (my_metadata_t *)mmap_from_system(buffer_size);
    metadata->size = buffer_size - sizeof(my_metadata_t);
    metadata->next = NULL;
    // Add the memory region to the free list.
    my_add_to_free_list(metadata, get_my_bin(metadata->size));
    my_bin_idx = num_of_bin - 1;
    // Now, try my_malloc() again. This should succeed.
    return my_malloc(size);
  }

  // |ptr| is the beginning of the allocated object.
  //
  // ... | metadata | object | ...
  //     ^          ^
  //     metadata   ptr
  void *ptr = metadata + 1;
  size_t remaining_size = metadata->size - size;
  metadata->size = size;
  // Remove the free slot from the free list.
  my_remove_from_free_list(metadata, prev, my_bin_idx - 1);

  if (remaining_size > sizeof(my_metadata_t)) {
    // Create a new metadata for the remaining free slot.
    //
    // ... | metadata | object | metadata | free slot | ...
    //     ^          ^        ^
    //     metadata   ptr      new_metadata
    //                 <------><---------------------->
    //                   size       remaining size
    my_metadata_t *new_metadata = (my_metadata_t *)((char *)ptr + size);
    new_metadata->size = remaining_size - sizeof(my_metadata_t);
    new_metadata->next = NULL;
    
    // Add the remaining free slot to the free list.
    my_add_to_free_list(new_metadata, get_my_bin(new_metadata->size));
  }
  return ptr;
}

// This is called every time an object is freed.  You are not allowed to
// use any library functions other than mmap_from_system / munmap_to_system.
void my_free(void *ptr) {
  // Look up the metadata. The metadata is placed just prior to the object.
  //
  // ... | metadata | object | ...
  //     ^          ^
  //     metadata   ptr
  my_metadata_t *metadata = (my_metadata_t *)ptr - 1;
  // Add the free slot to the free list.
  my_add_to_free_list(metadata, get_my_bin(metadata->size));
}

// This is called at the end of each challenge.
void my_finalize() {
  // Nothing is here for now.
  // feel free to add something if you want!
}

void test() {
  // Implement here!
  assert(1 == 1); /* 1 is 1. That's always true! (You can remove this.) */
}
