第一章：
    1.数据结构： 是相互之间存在一种或多种特定关系的数据元素的集合。
    2.四种基本结构:
        <1>.集合
        <2>.线性结构
        <3>.树形结构
        <4>.图状结构或网状结构
    3.数据类型是一个值的集合和定义在这个值集上的一组操作的总称。
    4.算法 Algorithm 是指对特定的问题求解步骤的一种描述，它是指令的有限序列，其中每一条指令表示一个或多个操作；
    5.算法的五个特性：有穷性 确定性 可行性 输入 输出
    6.算法设计的要求：正确性 可读性 健壮性 效率与低存储量需求 
    7.任何一个算法的设计取决于选定的数据（逻辑）结构，而算法的实现依赖于采用的存储结构
    8.归并算法：
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