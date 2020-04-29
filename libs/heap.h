#ifndef _HEAPQ_
#define _HEAPQ_
#include <stddef.h> /* size_t */
#include <stdint.h> /* uint8_t */
#include <stdlib.h> /* malloc free */

#define IDX2PTR(arr, i, sz)                                                    \
  ({                                                                           \
    uint8_t *_a = (uint8_t *)(arr)-sz;                                         \
    size_t _i = (i);                                                           \
    size_t _sz = (sz);                                                         \
    (void *)(_i * _sz + _a);                                                   \
  })

#define SWAP(a, b, size)                                                       \
  {                                                                            \
    size_t _size = (size);                                                     \
    uint8_t *_a = (a);                                                   \
    uint8_t *_b = (b);                                                   \
    while (_size--) {                                                          \
      uint8_t _t = *_a;                                                        \
      *_a++ = *_b;                                                             \
      *_b++ = _t;                                                              \
    }                                                                          \
  }
#define PUT(arr, i, x, size)                                                   \
  {                                                                            \
    size_t _sz = (size);                                                       \
    const uint8_t *_x = (x);                                                   \
    uint8_t *_a = IDX2PTR(arr, i, size);                                       \
    while (_sz--) {                                                            \
      *_a++ = *_x++;                                                           \
    }                                                                          \
  }

typedef int(cmp_fn)(const void *, const void *);

static void swim(void *const arr, size_t sz, size_t k, cmp_fn cmp) {
  while (k > 1) {
    void *cur = IDX2PTR(arr, k, sz);
    void *par = IDX2PTR(arr, k / 2, sz);

    if (cmp(cur, par) >= 0)
      break;

    SWAP(cur, par, sz);
    k /= 2;
  }
}

static void sink(void *const arr, size_t sz, size_t k, size_t len, cmp_fn cmp) {
  while (k * 2 <= len) {
    size_t small = k * 2; // left child
    if (small < len       // right exists
        && cmp(IDX2PTR(arr, small, sz), IDX2PTR(arr, small + 1, sz)) > 0) {
      // left is large than right
      small += 1;
    }

    void *cur = IDX2PTR(arr, k, sz);
    void *sptr = IDX2PTR(arr, small, sz);
    if (cmp(sptr, cur) >= 0) {
      // both children is large than or equal to `cur`
      break;
    }

    SWAP(cur, sptr, sz);
    k = small;
  }
}

/* heapify: make an arr be a heap
 * @sz: element size
 * @len: length of `arr`
 * @cmp: function pointer to compare elements in `arr`
 **/
void heapify(void *const arr, size_t sz, size_t len, cmp_fn cmp) {
  for (size_t i = len / 2; i > 0; i--) {
    sink(arr, sz, i, len, cmp);
  }
}

void heap_push(void *const arr, size_t sz, const void *x, size_t len,
               cmp_fn cmp) {
  PUT(arr, len + 1, x, sz);
  swim(arr, sz, len + 1, cmp);
}

void heap_pop(void *const arr, size_t sz, size_t len, cmp_fn cmp) {
  SWAP(IDX2PTR(arr, 1, sz), IDX2PTR(arr, len, sz), sz);
  len -= 1;
  sink(arr, sz, 1, len, cmp);
}

/* heapsort: sort `arr`
 * @sz: element size
 * @len: length of `arr`
 * @cmp: function pointer to compare elements in `arr`
 **/
void heap_sort(void *const arr, size_t sz, size_t len, cmp_fn cmp) {
  heapify(arr, sz, len, cmp);
  while (len > 1) {
    SWAP(IDX2PTR(arr, 1, sz), IDX2PTR(arr, len, sz), sz);
    len -= 1;
    sink(arr, sz, 1, len, cmp);
  }
}

#undef IDX2PTR
#undef SWAP
#undef PUT
#endif
