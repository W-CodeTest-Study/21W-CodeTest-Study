#include <iostream>
#include <string>

using std::cin;
using std::cout;
using std::endl;

#define lData char

class list
{
	private:
		class list* prev_node;
		class list* next_node;
		lData data;
	public:
		list(lData data)
			: data(data), prev_node(this), next_node(this)
		{}
		lData getData()
		{
			return data;
		}
		void setData(const lData data)
		{
			this->data = data;
		}
		void setNext(class list& rlist)
		{
			this->next_node = &rlist;
		}
		void setPrev(class list& rlist)
		{
			this->prev_node = &rlist;
		}
		class list* nextNode()
		{
			return next_node;
		}
		class list* prevNode()
		{
			return prev_node;
		}
};

class editor
{
	private:
		class list* cursor;
		class list* tail;
		int len;
	public:
		editor(class list& rlist)
			: cursor(&rlist), len(1)
		{}
		editor()
			: cursor(NULL), len(0)
		{}

		void initCur(class list& rlist) {
			cursor = &rlist;
			tail = &rlist;
		}

		void addLeft(class list& rlist)
		{
			rlist.setNext(*cursor);
			rlist.setPrev(*(cursor->prevNode()));

			cursor->prevNode()->setNext(rlist);
			cursor->setPrev(rlist);
			len++;
		}

		bool delCur()
		{
			if (cursor->prevNode() == tail)
				return false;
			class list* killer = cursor->prevNode();

			killer->prevNode()->setNext(*(killer->nextNode()));
			killer->nextNode()->setPrev(*(killer->prevNode()));

			delete killer;
			len--;
			return true;
		}

		bool moveLeft()
		{
			if (cursor->prevNode() == tail)
				return false;
			cursor = cursor->prevNode();
			return true;
		}
		bool moveRight()
		{
			if (cursor == tail)
				return false;
			cursor = cursor->nextNode();
			return true;
		}
		void printAll() {
			while (cursor->prevNode() != tail) {
				cursor = cursor->prevNode();
			}

			while (cursor != tail)
			{
				cout << cursor->getData();
				cursor = cursor->nextNode();
			}
		}
		~editor() {
			if (len)
				while(delCur());
		}
};

int main(void) {
	class editor ed;
	class list* tmp;
	char ch;
	int N;

	std::string str;

	tmp = new list('\0');
	ed.initCur(*tmp);

	getline(cin, str);

	for (int i = 0; i < str.size(); i++) {
		tmp = new list(str[i]);
		ed.addLeft(*tmp);
	}

	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> ch;
		switch(ch)
		{
			case 'L':
				ed.moveLeft();
				break;
			case 'D':
				ed.moveRight();
				break;
			case 'B':
				ed.delCur();
				break;
			case 'P':
				cin >> ch;
				tmp = new list(ch);
				ed.addLeft(*tmp);
				break;
		}
	}

	ed.printAll();
}
