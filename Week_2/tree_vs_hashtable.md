# Question 
木構造を使えばO(log N)、ハッシュテーブルを使えばほぼO(1)で検索・追加・削除を実現することができて、これだけ見ればハッシュテーブルのほうがはるかに優れているように見える。
ところが、現実の大規模なデータベースでは、ハッシュテーブルではなく木構造が使われることが多い。その理由を考えよ

The complexity of searching / adding / removing an element is mostly O(1) with a hash table, whereas the complexity is O(log N) with a tree. This means that a hash table is more efficient than a tree. However, real-world large-scale database systems tend to prefer a tree to a hash table. Why? List as many reasons as possible.

# My answers
1. **Nodes in a tree has a magnitude relationship whereas keys in a hashtable do not.** This means a tree supports some kinds of searches that are unavailable in a hashmap.
- range search
- min / max search
- relative search

2.  **The time complexity is fixed in a balanced tree.** The operation of adding or deleting an element is always done in O(logN) times in a balanced tree. In a hashtable, on the other hand, the operation of adding or deleting an element can be in O(1) time but it can be longer when there is duplicate keys.

3. **A tree does not need to be rebuilt even when the number of elements get bigger.** Engineers need to rebuild a hashmap when the amount of data is getting bigger so more duplicate keys are generated. The time complexity of adding or deleting an element is more than O(1) when there are duplicate keys. However, a balanced tree always takes O(logN) times, thereby there is no need to rebuild another hashtable.


