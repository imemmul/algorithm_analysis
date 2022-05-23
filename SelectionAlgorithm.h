#ifndef _SELECTIONALGORITHM_
#define _SELECTIONALGORITHM_



class SelectionAlgorithm {
    public:
        virtual int select();
        SelectionAlgorithm(int);
    protected:
        int k;
};

#endif