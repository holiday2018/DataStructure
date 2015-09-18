#结构体定义
struck Linknode{
    int data;
    struck Linknode *next;
}

#结构体定义
typedef struck Linknode Linklist;
#也可以用 struck Linknode Linlist;但不建议使用;

#初始化链表
int InitLinkList(Linklist **LNode){
    *LNode = (Linklist)malloc(sizeof(Linklist));
    if(!*LNode)
       return 0;
    (*LNode)->next = NULL;
    return 1;
}

#例程
int main(void){
    Linklist *L;
    InitLinklist(&L)
}
