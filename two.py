第二章：
    1.归并算法：
        void MergeList(List La, List Lb, List &Lc){
        //已知线性表La和Lb中的元素按值非递减排列。
        //归并La和Lb得到新的额线性表Lc，Lc中的数据元素也按值非递减排列
        InitList(Lc);
        i = j = 1; k = 0;
        La_len = ListLength(La); Lb_len = ListLength(Lb);
        while((i <= La_len) && (j < Lb_len)){
            GetElem(La, i, ai); GetElem(Lb, j, bj);
            if(ai <= bj) {ListInsert(Lc, ++k, ai); ++i;}
            else {ListInsert(Lc, ++k, bj); ++j;}
            }
        while (i < La_len){
            GetElem(La, i++, ai); ListInsert(Lc, ++k, ai);
            }
        while (j < Lb_len) {
            GetElem(Lb, j++, bj); ListInsert(Lc, ++k, bj);
            }
        }// MergeList
    2.线性表的元素插入算法：
    Status ListInsert_Sq(SqList &L, int i, ElemType e){
    //在线性表L中底i个位置之前插入新的元素额，
    //i的合法值为1 <= i <= Listlength_Sq(L) + 1
    if(i < 1 || i > L.length + 1) return ERROR; //i值不合法
    if (L.length > L.listsize) {                //当前存储空间已满，增加分派
        newbase = (ElemType *) realloc(L.elem, (L.listsize + LISTINCREMENT) * sizeof(ElemType));
        if(!newbase) exit(OVERFLOW);            //存储分配失败
        L.elem = newbase;                       //新基址
        L.listsize += LISTINCREMENT;            //增加存储容量
        }
     q = &(L.elem[i-1]);
     for(p = &(L.elem[L.length - 1]); p > = q; --p) *(P+1) = *p; //插入位置及之后的元素右移
     *q = e;        //插入e
     ++L.lenth;     //表长增1
     return OK;
    }//ListInsert_Sq  
    3.归并两个单链表的算法：
    void MergeList(LinkList &La, LinkList &Lb， LinkList &Lc){
    //已知单链线性表La和Lb的元素按值非递减排列。
    //归并La和Lb得到新的单链线性表Lc，Lc的元素也按值非递减排列
    pa = La->next; pb = Lb->next;
    Lc = pc = La;
    while(pa && pb){
        if(pa->data <= pb->data ){
            pc->next = pa; pc = pa; pa = pa->next;
            }
        else{pc->next = pb; pc = pb; pb = pb->next;}
        }
        pc->next = pa ? pa : pb; //插入剩余段
        free(Lb);                   //释放Lb的头节点
    }//MergeList_L