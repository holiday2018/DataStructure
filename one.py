��һ�£�
    1.���ݽṹ�� ���໥֮�����һ�ֻ�����ض���ϵ������Ԫ�صļ��ϡ�
    2.���ֻ����ṹ:
        <1>.����
        <2>.���Խṹ
        <3>.���νṹ
        <4>.ͼ״�ṹ����״�ṹ
    3.����������һ��ֵ�ļ��ϺͶ��������ֵ���ϵ�һ��������ܳơ�
    4.�㷨 Algorithm ��ָ���ض���������ⲽ���һ������������ָ����������У�����ÿһ��ָ���ʾһ������������
    5.�㷨��������ԣ������� ȷ���� ������ ���� ���
    6.�㷨��Ƶ�Ҫ����ȷ�� �ɶ��� ��׳�� Ч����ʹ洢������ 
    7.�κ�һ���㷨�����ȡ����ѡ�������ݣ��߼����ṹ�����㷨��ʵ�������ڲ��õĴ洢�ṹ
    8.�鲢�㷨��
        void MergeList(List La, List Lb, List &Lc){
        //��֪���Ա�La��Lb�е�Ԫ�ذ�ֵ�ǵݼ����С�
        //�鲢La��Lb�õ��µĶ����Ա�Lc��Lc�е�����Ԫ��Ҳ��ֵ�ǵݼ�����
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