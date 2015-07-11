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
    4.一维数组描述线性
        //-----线性表的静态单链表存储结构-----
        #define MAXSIZE 100         //链表的最大长度
        typedef struct {
            ElemEype data;
            int cure;
        }compoment, SLinkList[MAXSIZE];
        
        //将整个数组初始化成一个链表
        void InitSpace_SL(SLinkList &space){
            //将一维数组space中的个分量链成一个备用链表，space[0].cur为头指针
            //0 表示空指针
            int i;
            for(i = 0; i < MAXSIZE - 1; i++){
                space[i].cur = i + 1;
                }
            space[MAXSIZE - 1].cur = 0;
        }//InitSpace_SL
        
        //从备用空间取得一个节点
        int Malloc_SL(SLinkList &space){
            //若备用空间列表非空，则返回分配的节点下标，否则返回0
            i = space[0].cur;
            if(space[0].cur)space[0].cur = space[i].cur;
            return i;
            }//Malloc_SL
        
        //void Free_SL(SLinkList &space, int k){
            //将下标为k的节点回收到备用链表中
            space[k].cur = space[0].cur;
            space[0].cur = k;
            }//Free_SL
        
        //实现集合运算
        void difference(SLinkList &space, SLinkList &S){
            //以此输入集合A和B的元素，在一维数组space中建立集合（A-B）U（B-A）
            //的静态链表，S为其指针头。假设备用空间足够大，space[0].cur 为指针头
            InitSpace_SL(space);
            S = Malloc_SL(space);
            r = S;
            scanf(m,n);                 //输入A和B的元素个数
            for(j = 1; i < = m; ++j){   //建立集合A链表
                i = Malloc_SL(space);
                scanf(S[i].data);
                space[r].cur = i;
                r = i;
                }
            space[r].cur = 0;
            for(j = 1; i <= n; ++j){
                scanf(b); p = S; k = space[S].cur;
                while(k! = space[r].cur && space[k].data != b){
                    p = k; k = space[k].cur;
                    }
                if(k == space[r].cur){
                    i = Malloc_SL(space);
                    space[i].data = b;
                    space[i].cur = space[r].cur;
                    space[r].cur = i;
                    }
                else{
                    space[p].cur = space[k].cur;
                    Free_SL(space, k);
                    if(r == k) r = p; //若删除的是尾元素，则需要修改指针
                    }
                }
        }
        
        