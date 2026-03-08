#include <stdlib.h>

// Linked List Definitions
// ----------------------------------------------
typedef struct node {
    int          key;
    int          value;
    struct node* next;
    struct node* prev;
} node;

void  addLast     (node* head, node* tail, node* newNode);
void  moveToLast  (node* head, node* tail, node* ref);
node* removeFirst (node* head, node* tail);
void  freeList    (node* head);

// HashMap Definitions
// ----------------------------------------------
typedef struct dict_node {
    int               key;
    node*             value;
    struct dict_node* next;
} dict_node;

typedef struct {
    int         size;
    int         capacity;
    dict_node** buckets;
} dict;

void  dict_init   (dict* d);
node* dict_get    (dict* d, int key);
void  dict_remove (dict* d, int key);
void  dict_put    (dict* d, int key, node *value);
void  dict_free   (dict* d);

// Solution
// ----------------------------------------------
typedef struct {
    node* head;
    node* tail;
    dict  map;
    int   capacity;
} LRUCache;

LRUCache* lRUCacheCreate(int capacity) {
    LRUCache* obj = (LRUCache*)malloc(sizeof(LRUCache));
    
    obj->head = (node*)malloc(sizeof(node));
    obj->tail = (node*)malloc(sizeof(node));

    obj->head->next = obj->tail;
    obj->tail->prev = obj->head;

    obj->head->prev = NULL;
    obj->tail->next = NULL;
    
    dict_init(&obj->map);
    obj->capacity = capacity;
    
    return obj;
}

int lRUCacheGet(LRUCache* obj, int key) {
    node *n = dict_get(&obj->map, key);
    if (n == NULL)
        return -1;
    moveToLast(obj->head, obj->tail, n);
    return n->value;
}

void lRUCachePut(LRUCache* obj, int key, int value) {
    node *n = dict_get(&obj->map, key);
    if (n != NULL) {
        n->value = value;
        moveToLast(obj->head, obj->tail, n);
        return;
    }

    node *newNode = (node *)malloc(sizeof(node));
    newNode->key = key;
    newNode->value = value;

    if ((obj->map.size) >= (obj->capacity)) {
        node *lru = removeFirst(obj->head, obj->tail);
        dict_remove(&obj->map, lru->key);
        free(lru);
    }

    addLast(obj->head, obj->tail, newNode);
    dict_put(&obj->map, key, newNode);
}

void lRUCacheFree(LRUCache* obj) {
    dict_free(&obj->map);
    freeList(obj->head);
    obj->capacity = 0;
    obj->head = obj->tail = NULL;
    free(obj);
}

// Implementation
// ----------------------------------------------

// HashMap
// ----------------------------------------------
static int hashFn(int key, dict* d) {
    // keys will be positive (for the usecase)
    return key % d->capacity;
}

static void resize(dict *d) {
    dict_node** oldArray = d->buckets;
    int oldCap = d->capacity;

    d->capacity = 2 * oldCap;
    d->buckets = (dict_node **)calloc(d->capacity, sizeof(dict_node *));

    for (int i = 0; i < oldCap; i++) {
        dict_node* iter = oldArray[i];
        while (iter) {
            dict_node* nodeToRehash = iter;
            iter = iter->next;
            int bucketIndex = hashFn(nodeToRehash->key, d);
            nodeToRehash->next = d->buckets[bucketIndex];
            d->buckets[bucketIndex] = nodeToRehash;
        }
    }

    free(oldArray);
}

static dict_node* init_dict_node(int key, node *value) {
    dict_node* node = (dict_node *)malloc(sizeof(dict_node));
    node->key = key;
    node->value = value;
    node->next = NULL;
    return node;
}

void dict_init (dict *d) {
    d->capacity = 8;
    d->size = 0;
    d->buckets = (dict_node **)calloc(d->capacity, sizeof(dict_node *));
}

node *dict_get (dict *d, int key) {
    int bucketIndex = hashFn(key, d);

    dict_node* iter = d->buckets[bucketIndex];
    while (iter) {
        if (iter->key == key) {
            return iter->value;
        }
        iter = iter->next;
    }

    return NULL;
}

void dict_put (dict *d, int key, node *value) {
    if ((d->size) >= (d->capacity * 0.6)) {
        resize(d);
    }

    int bucketIndex = hashFn(key, d);

    dict_node* curr = d->buckets[bucketIndex];

    while (curr) {
        if (curr->key == key) {
            curr->value = value;
            return;
        }

        curr = curr->next;
    }

    dict_node* newNode = init_dict_node(key, value);
    newNode->next = d->buckets[bucketIndex];
    d->buckets[bucketIndex] = newNode;
    d->size++;
}

void dict_remove (dict *d, int key) {
    int bucketIndex = hashFn(key, d);

    dict_node* curr = d->buckets[bucketIndex];
    dict_node* prev = NULL;

    while (curr) {
        if (curr->key == key) {
            if (prev)
                prev->next = curr->next;
            else
                d->buckets[bucketIndex] = curr->next;
            free(curr);
            d->size--;
            return;
        }

        prev = curr;
        curr = curr->next;
    }
}

void dict_free (dict *d) {
    for (int i = 0; i < d->capacity; i++) {
        dict_node* iter = d->buckets[i];
        while (iter) {
            dict_node* to_delete = iter;
            iter = iter->next;
            free(to_delete);
        }
    }

    free(d->buckets);
    d->buckets = NULL;
    d->size = 0;
    d->capacity = 0;
}

// Linked List
// ----------------------------------------------
void moveToLast (node* head, node* tail, node* ref) {
    // unlink ref from chain
    node* r_prev = ref->prev;
    node* r_next = ref->next;

    r_prev->next = r_next;
    r_next->prev = r_prev;

    // all ref before tail
    node *t_prev = tail->prev;

    t_prev->next = ref;
    ref->prev = t_prev;

    ref->next = tail;
    tail->prev = ref;
}

void addLast (node* head, node* tail, node* newNode) {
    node* t_prev = tail->prev;

    t_prev->next = newNode;
    newNode->prev = t_prev;

    newNode->next = tail;
    tail->prev = newNode;
}

node* removeFirst (node* head, node* tail) {
    node* to_remove = head->next;

    head->next = to_remove->next;
    to_remove->next->prev = head;

    to_remove->next = to_remove->prev = NULL;

    return to_remove;
}

void freeList (node* head) {
    node* iter = head;
    while (iter) {
        node* to_delete = iter;
        iter = iter->next;
        free(to_delete);
    }
}
