#include <jni.h>
#include<stdio.h>
#include "A3.h"
JNIEXPORT int JNICALL Java_A3_add(JNIEnv *env,jobject obj,jint a,jint b){
    printf("\n%d+%d=%d\n",a,b,(a+b));
    return 0;
}
JNIEXPORT int JNICALL Java_A3_sub(JNIEnv *env,jobject obj,jint a,jint b){
    printf("\n%d-%d=%d\n",a,b,(a-b));
    return 0;
}
JNIEXPORT int JNICALL Java_A3_mul(JNIEnv *env,jobject obj,jint a,jint b){
    printf("\n%d*%d=%d\n",a,b,(a*b));
    return 0;
}
JNIEXPORT int JNICALL Java_A3_div(JNIEnv *env,jobject obj,jint a,jint b){
    printf("\n%d/%d=%d\n",a,b,(a/b));
    return 0;
}