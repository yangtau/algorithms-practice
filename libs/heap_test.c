#include "heap.h"
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print_arr(int arr[], size_t len) {
  for (size_t i = 0; i < len; i++) {
    printf("%d ", arr[i]);
  }
  printf("\n");
}

int int_cmp(const void *a, const void *b) {
  const int *_a = a;
  const int *_b = b;
  return *_a - *_b;
}
int int_cmp_q(const void *a, const void *b) {
  const int *_a = a;
  const int *_b = b;
  return *_b - *_a;
}

int check_sort(int *arr, size_t len) {
  int *b = malloc(sizeof(int) * len);
  memcpy(b, arr, len * sizeof(int));
  qsort(b, len, sizeof(int), int_cmp_q);
  return memcmp(arr, b, len * sizeof(int)) == 0;
}

int main() {
  {
    int arr[] = {2, 7, 4, 1, 8, 1};
    size_t len = sizeof(arr) / sizeof(int);
    heapify(arr, sizeof(int), len, int_cmp_q);
    print_arr(arr, len);
  }
  {
    int arr[100] = {4, 10, 6, 9, 0, -1, 7, -20, 3, 4};
    size_t len = 10;
    heapify(arr, sizeof(int), len, int_cmp);
  }
  {
    int arr[100] = {4, 10, 6, 9, 0, -1, 7, -20, 3, 4};
    size_t len = 10;
    heap_sort(arr, sizeof(int), len, int_cmp);
  }
  {
    size_t test_len = 10;
    for (size_t i = 0; i < test_len; i++) {
      size_t len = abs(rand()) % 200000;
      if (len == 0)
        len = 100;
      int *arr = malloc(sizeof(int) * len);
      for (size_t j = 0; j < len; j++) {
        arr[j] = rand();
      }
      heap_sort(arr, sizeof(int), len, int_cmp);
      assert(check_sort(arr, len));
      free(arr);
    }
  }
  {
    int arr[100] = {1, 10, 6, 9, 0, -1, 7, -20, 3, 4};
    size_t len = 10;
    heapify(arr, sizeof(int), len, int_cmp);
    assert(arr[0] == -20);

    heap_pop(arr, sizeof(int), len--, int_cmp);
    assert(arr[0] == -1);

    heap_pop(arr, sizeof(int), len--, int_cmp);
    assert(arr[0] == 0);

    heap_pop(arr, sizeof(int), len--, int_cmp);
    assert(arr[0] == 1);

    heap_pop(arr, sizeof(int), len--, int_cmp);
    assert(arr[0] == 3);

    heap_pop(arr, sizeof(int), len--, int_cmp);
    assert(arr[0] == 4);

    int x = -100;
    heap_push(arr, sizeof(int), &x, len++, int_cmp);
    assert(arr[0] == -100);

    heap_pop(arr, sizeof(int), len--, int_cmp);
    assert(arr[0] == 4);

    heap_pop(arr, sizeof(int), len--, int_cmp);
    assert(arr[0] == 6);

    heap_pop(arr, sizeof(int), len--, int_cmp);
    assert(arr[0] == 7);

    heap_pop(arr, sizeof(int), len--, int_cmp);
    assert(arr[0] == 9);

    heap_pop(arr, sizeof(int), len--, int_cmp);
    assert(arr[0] == 10);

    heap_pop(arr, sizeof(int), len--, int_cmp);

    x = 100;
    heap_push(arr, sizeof(int), &x, len++, int_cmp);
    assert(arr[0] == 100);

    x = 10;
    heap_push(arr, sizeof(int), &x, len++, int_cmp);
    assert(arr[0] == 10);

    x = 20;
    heap_push(arr, sizeof(int), &x, len++, int_cmp);
    assert(arr[0] == 10);

    x = 15;
    heap_push(arr, sizeof(int), &x, len++, int_cmp);
    assert(arr[0] == 10);

    x = 40;
    heap_push(arr, sizeof(int), &x, len++, int_cmp);
    assert(arr[0] == 10);

    x = -100;
    heap_push(arr, sizeof(int), &x, len++, int_cmp);
    assert(arr[0] == -100);

    x = -200;
    heap_push(arr, sizeof(int), &x, len++, int_cmp);
    assert(arr[0] == -200);

    heap_pop(arr, sizeof(int), len--, int_cmp);
    assert(arr[0] == -100);

    heap_pop(arr, sizeof(int), len--, int_cmp);
    assert(arr[0] == 10);

    heap_pop(arr, sizeof(int), len--, int_cmp);
    assert(arr[0] == 15);

    heap_pop(arr, sizeof(int), len--, int_cmp);
    assert(arr[0] == 20);

    heap_pop(arr, sizeof(int), len--, int_cmp);
    assert(arr[0] == 40);

    heap_pop(arr, sizeof(int), len--, int_cmp);
    assert(arr[0] == 100);
  }
  return 0;
}
