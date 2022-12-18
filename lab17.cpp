#include<iostream>
#include <string>

// Аналогично вводим дерево. Затем, появляется меню, где доступны операции добавления, удаления и поиска вершины.
// после выполнения программа опяь возвращается в меню. При выходе из него должно быть выведено БДН.
class Tree
{
public:
	int value;
	Tree* p;
	Tree* l;
	Tree* r;
	std::string string; 

	Tree(const int v, Tree* parent)
	{
		value = v;
		p = parent;
	}
	Tree()
	{

	}
	Tree(std::string str)
	{
		string = str;
	}

	void add(const int v)
	{
		if (v > value)
		{
			if (r == nullptr)
			{
				r = new Tree(v, this);
			}
			else
			{
				r->add(v);
			}
		}
		else
		{
			if (l == nullptr)
			{
				l = new Tree(v, this);
			}
			else
			{
				l->add(v);
			}
		}
	}

	Tree* search(Tree* item, int v) // поиск поддерева по элементу
	{
		if (item == nullptr && item->value == v)
		{
			return item;
		}
		if (item != nullptr && item->value > v)
		{
			return search(item->l, v);
		}
		if (item != nullptr && item->value < v)
		{
			return search(item->r, v);
		}
	}
	// переводит число в строку
	std::string toString(int value) 
	{
		std::string result;

		if (value > 9)
		{
			result += char(value / 10 + 48);
			result += char(value % 10 + 48);
		}
		else
		{
			result += char(value + 48);
		}

		return result;
	}

	// переводит дерево в линейно-скобочуню запись
	void print(Tree* tree) 
	{
		string += toString(tree->value);
		if (tree->l != nullptr || tree->r != nullptr)
		{
			string += '(';
			if (tree->l != nullptr)
			{
				print(tree->l);
			}
			string += ',';
			if (tree->r != nullptr)
			{
				print(tree->r);
			}
			string += ')';
		}

	}

	Tree* Search(int v)
	{
		return search(this, v);
	}

	void remove(int value)
	{
		Tree* item = this->Search(value);
		if (item == nullptr) return;
		Tree* currentTree = nullptr;
		// удаление корня
		if (this == item)
		{
			if (item->r != nullptr)
			{
				currentTree = item->r;
				while (currentTree->l != nullptr)
				{
					currentTree = currentTree->l;
				}

			}
			else if (item->l != nullptr)
			{
				currentTree = item->l;
				while (currentTree->r != nullptr)
				{
					currentTree = currentTree->r;
				}
			}

			int val = currentTree->value;
			remove(val);
			item->value = val;

		}
		// удаление листьев
		else if (item->l == nullptr && item->r == nullptr && item->p != nullptr)
		{
			if (item->p->r == item)
			{
				item->p->r = nullptr;
			}
			else
			{
				item->p->l = nullptr;
			}
		}
		// удаление узла, который имеет левого потомка.
		else if (item->l != nullptr && item->r == nullptr && item->p != nullptr)
		{
			item->l->p = item->p;
			if (item == item->p->l)
			{
				*item->p->l = *item->l;
			}
			else if (item == item->p->r)
			{
				*item->p->r = *item->l;
			}

		}
		// удаление узла, который имеет правого потомка.
		else if (item->l == nullptr && item->r != nullptr && item->p != nullptr)
		{
			item->r->p = item->p;
			if (item == item->p->l)
			{
				*item->p->l = *item->r;
			}
			else if (item == item->p->r)
			{
				*item->p->r = *item->r;
			}

		}
		// удаление узла, который имеет оба потомка.
		else if (item->l != nullptr && item->r != nullptr && item->p != nullptr)
		{
			currentTree = item->r;
			if (currentTree->l != nullptr)
			{
				while (currentTree->l != nullptr)
				{
					currentTree = currentTree->l;
				}
				if (currentTree->r != nullptr)
				{
					currentTree->r->p = currentTree->p;
					currentTree->p->l = currentTree->r;
				}
				else
				{
					currentTree->p->l = nullptr;
				}
				item->l->p = currentTree;
				currentTree->l = item->l;
				if (item->p->r == item)
				{
					currentTree->p = item->p->r;
					item->p->r = currentTree;
				}
				else
				{
					currentTree->p = item->p->l;
					item->p->l = currentTree;
				}
				currentTree->r = item->r;
				item->r->p = currentTree;
			}
			else
			{
				item->l->p = currentTree;
				currentTree->l = item->l;
				currentTree->p = item->p;
				if (item->p->l == item)
				{
					item->p->l = currentTree;
				}
				else
				{
					item->p->r = currentTree;
				}
			}

		}


	}
	void Print()
	{
		print(this);
	}

	bool isDigital(const char elem)
	{
		return (elem >= '0' && elem <= '9') ? true : false;
	}

	// строка в бинарное дерево
	Tree parse(std::string str) 
	{
		Tree result;
		int index;
		if (isDigital(str[0]) && isDigital(str[1]))
		{
			int val = (str[0] - 48) * 10 + str[1] - 48;
			result.value = val;
			index = 2;
		}
		else if (isDigital(str[0]) && !isDigital(str[1]))
		{
			int val = str[0] - 48;
			result.value = val;
			index = 1;
		}


		for (int i = index; i < str.size() - 1;)
		{
			if (isDigital(str[i]) && isDigital(str[i + 1]))
			{
				int value = (str[i] - 48) * 10 + str[i + 1] - 48;
				result.add(value);
				i += 2;
			}
			else if (isDigital(str[i]) && !isDigital(str[i + 1]))
			{
				int value = str[i] - 48;
				result.add(value);
				i++;
			}
			else
			{
				i++;
			}
		}
		return result;
	}
};



void main()
{
	std::string str = "8(3(1,6(4,7)),10(,14(13,)))";
	Tree tree;
	tree = tree.parse(str);
	Tree newTree = tree;
	newTree.remove(10);
	newTree.Print();
	for (auto& value : newTree.string)
	{
		std::cout << value;
	}
	std::cout << "Choose command: 1) add element, 2) remove element, 3)show tree by element" << std::endl;
	int n = -1;
	while (n != 0)
	{
		std::cin >> n;
		switch (n)
		{
		case 1:
		{
			int value;
			std::cout << "Input value to add:";
			std::cin >> value;
			newTree.add(value);
			newTree.Print();

			for (auto& value : newTree.string)
			{
				std::cout << value;
			}
			newTree.string = "";
			break;

		}
		case 2:
		{
			int value;
			std::cout << "Input value to remove:";
			std::cin >> value;
			newTree.remove(value);
			newTree.Print();

			for (auto& value : newTree.string)
			{
				std::cout << value;
			}
			newTree.string = "";
			break;
		}
		case 3:
		{
			newTree.Print();
			for (auto& value : newTree.string)
			{
				std::cout << value;
			}
			newTree.string = "";
			break;
		}
		default:
		{
			newTree.Print();
			for (auto& value : newTree.string)
			{
				std::cout << value;
			}
			newTree.string = "";
			break;
		}
		}

	}

}