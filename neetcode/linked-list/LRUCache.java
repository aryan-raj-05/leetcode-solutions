import java.util.HashMap;

// Problem 146: LRU Cache
class LRUCache {
    private Node head = new Node();
    private Node tail = new Node();
    private HashMap<Integer, Node> map = new HashMap<>();
    private int capacity;

    public LRUCache(int capacity) {
        head.next = tail;
        tail.prev = head;
        this.capacity = capacity;
    }
    
    public int get(int key) {
        if (!map.containsKey(key)) {
            return -1;
        }

        Node node = map.get(key);
        moveToLast(node);

        return node.value;
    }
    
    public void put(int key, int value) {
        if (map.containsKey(key)) {
            Node n = map.get(key);
            n.value = value;
            moveToLast(n);
            return;
        }
        
        Node newNode = new Node(key, value);

        if (map.size() >= capacity) {
            var lru = removeFirst();
            map.remove(lru.key);
        }

        addLast(newNode);
        map.put(key, newNode);
    }

    private void addLast(Node ref) {
        Node penul = tail.prev;
        penul.next = ref;
        ref.prev = penul;
        ref.next = tail;
        tail.prev = ref;
    }

    private void moveToLast(Node ref) {
        // unlink from the chain
        Node p = ref.prev;
        Node n = ref.next;
        p.next = n;
        n.prev = p;

        // move ref to last
        Node last = tail.prev;
        last.next = ref;
        ref.prev = last;
        ref.next = tail;
        tail.prev = ref;
    }

    private Node removeFirst() {
        Node n = head.next;
        head.next = n.next;
        n.next.prev = head;
        n.next = null;
        n.prev = null;

        return n;
    }

    private static class Node {
        int key;
        int value;
        Node next;
        Node prev;

        Node () {}

        Node(int key, int value) {
            this.key = key;
            this.value = value;
            this.next = null;
            this.prev = null;
        }
    }
}
