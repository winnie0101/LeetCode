#include <stdio.h>
#include <stdlib.h>
#define TABLE_SIZE 50000

typedef struct HashNode {
    int key; 
    int count;
    struct HashNode* next;
} HashNode;

unsigned int hash(int key) {
    return abs(key) % TABLE_SIZE;
}

void insertOrUpdate(HashNode* hashTable[], int key) {
    unsigned int index = hash(key);
    HashNode* node = hashTable[index];

    while (node != NULL) {
        if (node->key == key) {
            node->count++;
            return;
        }
        node = node->next;
    }
    HashNode* newNode = (HashNode*)malloc(sizeof(HashNode));
    newNode->key = key;
    newNode->count = 1;
    newNode->next = hashTable[index];
    hashTable[index] = newNode;
}

int getCount(HashNode* hashTable[], int key) {
    unsigned int index = hash(key);
    HashNode* node = hashTable[index];

    while (node != NULL) {
        if (node->key == key) {
            return node->count;
        }
        node = node->next;
    }
    return 0;
}

void freeTable(HashNode** hashTable) {
    for (int i = 0; i < TABLE_SIZE; i++) {
        HashNode* node = hashTable[i];
        while (node != NULL) {
            HashNode* temp = node;
            node = node->next;
            free(temp);
        }
    }
}

int majorityElement(int* nums, int numsSize) {
    int max_time = numsSize / 2;
    HashNode* hashTable[TABLE_SIZE] = {NULL};
    for (int i = 0; i < numsSize; i++) {
        insertOrUpdate(hashTable, nums[i]);
        if (getCount(hashTable, nums[i]) > max_time) {
            return nums[i];
        }
    }
    freeTable(hashTable);
    return -1;
}

int main() {
    int nums[] = {2,2,1,1,1,2,2};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int max_time = numsSize / 2;
    printf("%d\n", majorityElement(nums, numsSize, max_time));
    return 0;
}