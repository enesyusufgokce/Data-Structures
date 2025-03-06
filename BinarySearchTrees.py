"""
The biggest advantage of a BST is that it allows fast access, search, insertion, and deletion operations
with a time complexity of O(log n). When the tree is balanced, each insertion and search operation takes time
proportional to the tree height. In the worst case (e.g., in an unbalanced BST where elements are inserted
sequentially), the complexity can be O(n)

All the keys in the left subtree are less than the key in the root
All the keys in the right subtree are greater than the root

        70
       /  \
     31    93
    /     /  \
  14    73    94
    \
     23

"""

"""
Insertion
Search
Min & Max
Successor & Predecessor
Deletion
Number of nodes and tree height
Balance Check
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        if value > node.value:
            if node.right is None:
                node.right =TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):     # _ ile başlayan fonksiyonlar, private olarak yazılır genelde yani
        if node is None or node.value == value:   # kullanıcı tarafından çağrılamazlar , amaç güvenlik
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def find_min(self, node = None):  # node verilirse o node den başlayan subtree nin min değeri bulumur,  O(log n)
        if node is not None:          # verilmezse yani parametre girmezsek root tan başlar atamaya ve sonuçlar farklı olabilir
            current = node          # if node is give as parameter, process starts at this node
        else:                       # if it is not, process starts at the root node
            current = self.root
        while current and current.left:     # because left child is smaller
            current = current.left
        return current

    def find_max(self, node = None):           # O(log n)
        if node is not None:
            current = node
        else:
            current = self.root
        while current and current.right:
            current = current.right
        return current

    def find_successor(self, value):        # Successor, o düğümden büyük en küçük düğüm         O(log n)
        node = self.search(value)
        if node is None:
            return None
        if node.right:
            return self.find_min(node.right)      # right subtree si varsa ordan find_min çağır (node.right dahil)
        successor = None
        current = self.root
        while current:
            if value < current.value:
                successor = current
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                break
        return successor

    def find_predecessor(self, value):      # predecessor, o düğümden küçük en büyük düğümdür      O(log n)
        node = self.search(value)
        if node is None:
            return None
        if node.left:
            return self.find_max(node.left)          # left subtree si varsa ordan find_max çağır (node.left dahil)
        predecessor = None
        current = self.root
        while current:
            if value > current.value:
                predecessor = current
                current = current.right
            elif value < current.value:
                current = current.left
            else:
                break
        return predecessor

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)       # silmek istediğimiz node a ilerletiyor bizi
        elif value > node.value:                                       # ta ki ulaşana kadar
            node.right = self._delete_recursive(node.right, value)
        else:                                                          # silmek istediğimiz node dayız şuan
            # one child or no child
            if node.left is None:    # node.left e return edilen node.right değeri atandı aşağıdaki örnekte ve derinden yüzeye
                return node.right    # doğru çıkılmaya başlandı. kademe kademe içeri girdi, işlemi yaptı, dışarı doğru çıkıyor
            elif node.right is None:   # dışarı çıkarken fibonacci deki gibi çıkarkenki işlemi çok somut değil ama yine de
                return node.left       # işlevini yapıyor. işlevi sadece dışarı çıkmak çünkü.  fibonaccide toplayarak çıkmak
            # two child. find successor
            successor = self.find_successor(node.value)     # _delete_recursive de parametre olarak verilen node nin valuesi
            node.value = successor.value
            node.right = self._delete_recursive(node.right, successor.value)   # successor istenilen yere kondu ve successor
        # olarak kullanılan kısım silindi. node.right dememizin nedeni, bizim şuan için sadece two child li duruma bakıyor olmamız

        return node    #  Eğer return node sadece else bloğunun içinde olursa, recursive çağrılar sonucunda
                       #  güncellenen düğümleri geri dönüşte yerine koyamaz. yani geri dönüşte sıkıntı yaşar.

    def tree_height(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return -1
        return max(self.tree_height(node.left), self.tree_height(node.right)) + 1   # returns the largest of two or more given values
        # node=None dediği kısım, eğer node için bir parametre verilmemişse çalışır

    def count_nodes(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)    # + 1,  node un kendisini sayar

    def is_balanced(self, node=None):
        if node is None:
            node = self.root
        return self._check_balance(node) != -1

    def _check_balance(self, node):
        if node is None:
            return 0
        left_height = self._check_balance(node.left)
        right_height = self._check_balance(node.right)
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1

    # abs(left_height - right_height) > 1 koşulu ilk defa sağlandığında -1 döndürülür ve bu yukarıya taşınır
    # dibe indi, tekrar yukarı çıkıyor u sırada -1 değeri yukarıya taşınır. geldiği node ye atanıyor yani. ör: left_height


bst = BinarySearchTree()
bst.insert(15)
bst.insert(85)
bst.insert(18)
bst.insert(26)
bst.insert(25)
bst.insert(30)




r"""  
an example:

     10
    /  \  
   5    15
       /
      12
        \
         13   <-- 12'yi siliyoruz. 
"""
"""
return bir çağrıyı sonlandırıyor, ama üst fonksiyona bir değer döndürüyor.
Recursive fonksiyon kendi kendini çağırdığı için, önce en derine kadar gidiyor, 
sonra geri dönerek yukarıdaki düğümleri güncelliyor.

İlk olarak en alt seviyeye kadar çağrılar gidiyor.
Sonra, geri dönüş sırasında döndürülen değerler, üst seviyelerdeki referansları güncelliyor.

"""
