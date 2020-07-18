#pragma once
#include "Maplist.h"

using std::vector;


template<class T>
class mmergeSort
{
public:
	mmergeSort(vector<mapNode<T>*>& a) {
		this->temp.resize(a.size());
		mergeSortSubInterval(a, 0, a.size() - 1);
	}
	static void mergeSortSubInterval(vector<mapNode<T>*>& a, int low, int high) {
		if (high <= low)
			return;
		int mid = (high + low) / 2;
		mergeSortSubInterval(a, low, mid);
		mergeSortSubInterval(a, mid + 1, high);
		Merge(a, low, mid, high);
	}
	static void Merge(vector<mapNode<T>*>& a, int low, int mid, int high) {
		int i = low, j = mid + 1;
		for (int k = low; k <= high; k++)
			temp[k] = a[k];
		if (low == 0 && high == 8)
			int kkki = 1;
		for (int k = low; k <= high; k++) {
			if (i > mid) a[k] = temp[j++];
			else if (j > high) a[k] = temp[i++];
			else if ((temp[i]->element) < (temp[j]->element)) a[k] = temp[i++];
			else   a[k] = temp[j++];
		}
	}
private:
	static vector<mapNode<T>*> temp;
};
template<class T>
vector<mapNode<T>*> mmergeSort<T>::temp = {};


template<class T>
class qquickSort {
public:
	qquickSort(vector<mapNode<T>*>& a) {
		sort(a, 0, a.size() - 1);
	}

	static	void sort(vector<mapNode<T>*>& a, int low, int high) {
		if (high <= low)
			return;
		int j = partition(a, low, high);
		sort(a, low, j - 1);
		sort(a, j + 1, high);
	}

	static int partition(vector<mapNode<T>*>& a, int low, int high) {
		int i = low, j = high + 1;
		mapNode<T>*  v = a[low];
		while (1)
		{
			while ((a[++i]->element) < (v->element))
				if (i == high)
					break;
			while ((v->element) < (a[--j]->element))
				if (j == low)
					break;
			if (i >= j)
				break;
			mapNode<T>* temp = a[i];
			a[i] = a[j];
			a[j] = temp;
		}
		mapNode<T>* temp = a[low];
		a[low] = a[j];
		a[j] = temp;
		return j;
	}
};

template<class T>
class qquickSort1 {    //dijkstra提出的快排方案，效率比快排低不少
public:
	qquickSort1(vector<mapNode<T>*>& a) {
		sort(a, 0, a.size() - 1);
	}

	static void sort(vector<mapNode<T>*>& a, int low, int high) {
		if (high <= low)
			return;
		int lt = low, i = low + 1, gt = high;
		mapNode<T>* v = a[low];
		while (i <= gt)
		{
			if ((a[i]->element) < (v->element))
			{
				mapNode<T>* temp = a[lt];
				a[lt] = a[i];
				a[i] = temp;
				lt++, i++;
			}
			else if ((a[i]->element) > (v->element))
			{
				mapNode<T>* temp = a[i];
				a[i] = a[gt];
				a[gt] = temp;
				gt--;
			}
			else
				i++;
		}
		sort(a, low, lt - 1);
		sort(a, gt + 1, high);
	}
};


template<class T>
class hheapSort {    //堆排序
public:
	hheapSort(vector<mapNode<T>*>& a) {
		int N = a.size();
		N--;
		for (int k = N / 2 + 2; k >= 0; k--)
			sink(a, k, N);
		while (N > 0) {
			mapNode<T>* temp = a[N];
			a[N] = a[0];
			a[0] = temp;
			N--;
			sink(a, 0, N);
		}
	}

	static void sink(vector<mapNode<T>*>& a, int k, int N) {
		while (2 * k + 1 < N)
		{
			int j = 2 * k + 1;
			if (j + 1 < N && ((a[j]->element) < (a[j + 1]->element)))
				j++;
			if ((a[k]->element) >= (a[j]->element))
				break;
			mapNode<T>* temp = a[k];
			a[k] = a[j];
			a[j] = temp;
			k = j;
		}
	}
};

template<class T>
class Sort
{
public:
	static void  changeChain(mapList<T>& object, vector<mapNode<T>*> a, int N);  //用vector记录的指针重新编排链表
	void bubbleSort(mapList<T>& object);		//冒泡排序
	void bubbleSort1(mapList<T>& object);     //之前写的冒泡排序版本，因为进行的交换次数过多效率不如bubbleSort
	void insertSort(mapList<T>& object);		//插入排序		
	void shellSort(mapList<T>& object);			//希尔排序
	void mergeSort(mapList<T>& object);			//归并排序
	void quickSort(mapList<T>& object);			//快速排序
	void quickSort1(mapList<T>& object);		//据说为Dijkstra改进的快速排序，但实测效率不增反降
	void heapSort(mapList<T>& object);			//堆排序
};

template<class T>
inline void Sort<T>::changeChain(mapList<T>& object, vector<mapNode<T>*> a, int N)
{
	object.changeFistNode(a[0]);
	mapNode<T>* temp = object.getFirstNode();
	for (size_t i = 1; i < N; i++)
	{
		temp->next = a[i];
		temp = temp->next;
	}
	temp->next = nullptr;
}

template<class T>
void Sort<T>::bubbleSort(mapList<T>& object)
{
	vector<mapNode<T>*> a = {};
	auto p = object.getFirstNode();
	while (p)
	{
		a.push_back(p);
		p = p->next;
	}
	int N = object.getSize();    //  a的长度 
	for (size_t i = 0; i < N; i++) {
		int index = i;
		for (size_t j = i + 1; j < N; j++) {
			if (a[j]->element < a[index]->element)      //记录下每个i后方最小的a[j]的坐标
				index = j;
		}
		mapNode<T>* temp = a[index];
		a[index] = a[i];
		a[i] = temp;			//然后进行交换
	}
	changeChain(object, a, N);
}

template<class T>
void Sort<T>::bubbleSort1(mapList<T>& object)
{
	vector<mapNode<T>*> a = {};
	auto p = object.getFirstNode();
	while (p)
	{
		a.push_back(p);
		p = p->next;
	}
	int N = a.size();    //  a的长度 
	for (size_t i = 0; i < N; i++) {
		for (size_t j = i + 1; j < N; j++) {
			if ((a[j]->element) < (a[i]->element)) {
				mapNode<T>* temp = a[j];
				a[j] = a[i];
				a[i] = temp;
			}
		}
	}
	changeChain(object, a, N);
}

template<class T>
void Sort<T>::bubbleSort2(mapList<T>& object)
{
}

template<class T>
void Sort<T>::insertSort(mapList<T>& object)
{
	vector<mapNode<T>*> a;
	auto p = object.getFirstNode();
	while (p)
	{
		a.push_back(p);
		p = p->next;
	}
	int N = object.getSize();    //  a的长度 ;
	for (int i = 0; i < N; i++)
	{
		for (int j = i; (j > 0) && ((a[j]->element) < (a[j - 1]->element)); j--){//将每个a[j]往后插到合适的位置
			mapNode<T>* temp = a[j];
				a[j] = a[j - 1];
				a[j - 1] = temp;
		}
	}
	changeChain(object, a, N);
}

template<class T>
void Sort<T>::shellSort(mapList<T>& object)
{
	vector<mapNode<T>*> a;
	auto p = object.getFirstNode();
	while (p)
	{
		a.push_back(p);
		p = p->next;
	}
	int N = object.getSize();    //  a的长度 ;
	int h = 1;
	while (h < N / 3)
		h = 3 * h + 1;           //找到合适的初始值h
	while (h >= 1) {			//不断缩小h，对每个间隔h的小区间进行排序	
		for (int i = h; i < N; i++)
		{
			for (int j = i; j >= h && ((a[j]->element) < (a[j - h]->element)); j -= h)
			{
				mapNode<T>* temp = a[j];
				a[j] = a[j - h];
				a[j - h] = temp;
			}
		}
		h = h / 3;
	}
	changeChain(object, a, N);
}

template<class T>
void Sort<T>::mergeSort(mapList<T>& object)
{
	vector<mapNode<T>*> a;
	int N = object.getSize();
	auto p = object.getFirstNode();
	while (p)
	{
		a.push_back(p);
		p = p->next;
	}
	mmergeSort<T> yy(a);
	changeChain(object, a, N);
}

template<class T>
void Sort<T>::quickSort(mapList<T>& object)
{
	vector<mapNode<T>*> a;
	int N = object.getSize();
	auto p = object.getFirstNode();
	while (p)
	{
		a.push_back(p);
		p = p->next;
	}
	qquickSort<T>  yy(a);
	changeChain(object, a, N);

}

template<class T>
void Sort<T>::quickSort1(mapList<T>& object)
{
	vector<mapNode<T>*> a;
	int N = object.getSize();
	auto p = object.getFirstNode();
	while (p)
	{
		a.push_back(p);
		p = p->next;
	}
	qquickSort1<T>  yy(a);
	changeChain(object, a, N);
}

template<class T>
void Sort<T>::heapSort(mapList<T>& object)
{
	vector<mapNode<T>*> a;
	int N = object.getSize();
	auto p = object.getFirstNode();
	while (p)
	{
		a.push_back(p);
		p = p->next;
	}
	hheapSort<T>  yy(a);
	changeChain(object, a, N);
}

