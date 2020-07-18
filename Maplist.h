#pragma once
#include <stdexcept>
#include <iostream>
#include <vector>


using std::vector;
using std::cout;

template <class T>
struct mapNode
{
	T element;                      //节点内储存的数据
	mapNode<T>* next;				//下一个节点
	//构造函数
	mapNode<T>() {};
	mapNode<T>(const T& eelement, mapNode<T>* nnext = nullptr) {
		this->element = eelement; this->next = nnext;
	}
};


template <class T>
class mapList
{
private:
	int listSize;          //链长
	mapNode<T>* firstNode;		//头结点。注意！此链表结构头结点即存放第一个数据！
public:
	mapList();						//构造函数
	~mapList() {};					//析构函数
	void createMapList(vector<T> a);        //用vector数组创建链表
	inline mapNode<T>* getFirstNode() const { return firstNode; }	//返回头结点
	inline int getSize() const { return listSize; }		//返回长度
	void changeFistNode(mapNode<T>* newFirstNode);
	void insertMaplist(int theIndex, const T& theElement);  //以0为起始下标插入数据
	void deleteMapListByIndex(int theIndex);		//删除下标为 theInex的节点
	void deleteMapListByElement(const T& theElement);	//删除数据等于theElement的节点
	void pushBack(const T& theElement);  //在最后方增加新的节点
	void pop();  //删除最后一个节点
	mapList(const mapList<T>& theList);  //复制链表
	void destoryMaplist();    //销毁链表
	inline bool empty() const { return listSize == 0; } //返回bool值表达该链表是否为空
	vector<int> indexOf(const T& theElement) const; //返回数据为theElement的节点的下标。
};

template<class T>
mapList<T>::mapList()
{
	this->firstNode = nullptr;
	this->listSize = 0;
}

template<class T>
void mapList<T>::createMapList(vector<T> a)
{
	int N = a.size();
	this->listSize = N;
	if (!N) {
		this->firstNode = nullptr;
		this->listSize = 0;
		return;
	}
	this->firstNode = new mapNode<T>(a[0]);
	mapNode<T>* p = this->firstNode;
	for (size_t i = 1; i < N; i++) {
		p->next = new mapNode<T>(a[i]);
		p = p->next;
	}
}


template<class T>
mapList<T>::mapList(const mapList<T>& theList) //复制函数
{
	this->listSize = theList.listSize;
	if (!this->listSize) {
		this->firstNode = nullptr;
		return;
	}
	mapNode<T>* sourceNode = theList.firstNode;
	mapNode<T>* p = new mapNode<T>(theList.firstNode->element);
	sourceNode = sourceNode->next;
	this->firstNode = p;
	mapNode<T>* q = theList.firstNode;
	while (q->next)
	{
		p->next = q->next;
		p = p->next;
		q = q->next;
	}
	p->next = nullptr;
}

template<class T>
void mapList<T>::destoryMaplist() {
	while (this->firstNode)
	{
		mapNode<T>* nextNode = firstNode->next;
		free(this->firstNode);
		this->firstNode = nextNode;
	}
	this->~mapList();
}

template<class T>
vector<int> mapList<T>::indexOf(const T& theElement) const
{
	vector<int> ans = {};
	int ct = 0;
	auto i = this->firstNode;
	while (i)
	{
		if (i->element == theElement)
			ans.push_back(ct);
		i = i->next;
		ct++;
	}
	return ans;
}


template<class T>
inline void mapList<T>::pop()
{
	if (!this->listSize)
		throw  "the index out of range";
	else if (this->listSize-- == 1)
		this->firstNode = nullptr;
	else {
		mapNode<int>* p = this->firstNode;
		while (p->next->next)
			p = p->next;
		free(p->next);
		p->next = nullptr;
	}
}

template<class T>
void mapList<T>::pushBack(const T& theElement)
{
	if (!this->listSize++) {
		this->firstNode = new mapNode<T>(theElement);
		return;
	}
	mapNode<T>* newone = new mapNode<T>(theElement);
	mapNode<T>* p = this->firstNode;
	while (p->next)
		p = p->next;
	p->next = newone;
}


template<class T>
inline void mapList<T>::changeFistNode(mapNode<T>* newFirstNode)
{
	newFirstNode->next = this->firstNode;
	this->firstNode = newFirstNode;
}

template<class T>
inline void mapList<T>::insertMaplist(int theIndex, const T& theElement)
{
	if (theIndex < 0 || theIndex > this->listSize) {
		throw  "the index out of range";
	}
	this->listSize++;
	int i = 0;
	if (!theIndex) {
		mapNode<T>* temp = new mapNode<int>(theElement);
		temp->next = this->firstNode;
		this->firstNode = temp;
		return;
	}
	mapNode<T>* temp = this->firstNode;
	for (int i = 0; i < theIndex - 1; i++)
		temp = temp->next;
	mapNode<T>* newone = new mapNode<int>(theElement);
	newone->next = temp->next;
	temp->next = newone;
}

template<class T>
void mapList<T>::deleteMapListByIndex(int theIndex)
{
	if (theIndex < 0 || theIndex >= this->listSize)
		throw "theIndex erro";
	if (!theIndex) {
		auto p = this->firstNode;
		this->firstNode = this->firstNode->next;
		free(p);
		return;
	}
	auto p = this->firstNode;
	for (int i = 0; i < theIndex; i++)
		p = p->next;
	p->next = p->next->next;
}

template<class T>
void mapList<T>::deleteMapListByElement(const T& theElement)
{
	while (this->firstNode->element == theElement)
	{
		auto temp = this->firstNode;
		this->firstNode = temp->next;
		free(temp);
	}
	auto p = this->firstNode;
	while (p->next)
	{
		if (p->next->element == theElement) {
			auto temp = p->next;
			p->next = temp->next;
			free(temp);
		}
		p = p->next;
	}
}
