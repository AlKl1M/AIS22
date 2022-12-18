#include <iostream>
#include <stack>
#include <string>
#include <vector>

// условие аналогичное предыдущему, однако реализуем прямой обход (с помощью стека). 
class Tree
{
public:
	int value;
	Tree* p;
	Tree* l;
	Tree* r;
	std::string string; 
	//constr
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

	//добавление
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

	// преобразование дерева в линейно-скобочную для вывода
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


	void Print()
	{
		print(this);
	}

	// проверка на число
	bool isDigital(const char elem)
	{
		return (elem >= '0' && elem <= '9') ? true : false;
	}

	// Функция для прохода по строке и преобразования ее в бинарное дерево
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

// прямой обход
void direct(std::vector<int>& v, Tree* tree)
{
	std::stack <Tree*> s;
	s.push(nullptr);
	Tree* tempTree = tree;
	do
	{
		if (tempTree != nullptr)
		{
			s.push(tempTree);
			v.push_back(tempTree->value);
			tempTree = tempTree->l;
		}
		else
		{
			if (s.top() == nullptr)
			{
				break;
			}
			tempTree = s.top();
			s.pop();
			tempTree = tempTree->r;
		}
	} while (true);
}

// обратный обход
void reverse(std::vector<int>& v, Tree* tree)
{
	std::stack <Tree*> s;
	Tree* lastVisited = nullptr;
	Tree* tempTree = tree;
	while (!s.empty() || tempTree != nullptr)
	{
		if (tempTree != nullptr)
		{
			s.push(tempTree);
			tempTree = tempTree->l;
		}
		else
		{
			Tree* topTree = s.top();
			if (topTree->r != nullptr && lastVisited != topTree->r)
			{
				tempTree = topTree->r;
			}
			else
			{
				v.push_back(topTree->value);
				lastVisited = s.top();
				s.pop();
			}
		}
	}
}

// кольцевой
void center(std::vector<int>& v, Tree* tree)
{
	std::stack <Tree*> s;
	s.push(nullptr);
	Tree* tempTree = tree;
	do
	{
		if (tempTree != nullptr)
		{
			s.push(tempTree);
			tempTree = tempTree->l;
		}
		else
		{
			if (s.top() == nullptr)
			{
				break;
			}
			tempTree = s.top();
			s.pop();
			v.push_back(tempTree->value);
			tempTree = tempTree->r;
		}
	} while (true);
}


void main()
{

	std::vector <int> dV;
	std::vector <int> cV;
	std::vector <int> rV;
	int maxElem;
	std::string str = "8(3(1,6(4,7)),10(,14(13,)))";
	Tree tree;
	tree = tree.parse(str);
	Tree newTree = tree;
	newTree.Print();

	direct(dV, &newTree); 
	center(cV, &newTree);
	reverse(rV, &newTree);

	for (auto& value : rV)
	{
		std::cout << value << "\t";
	}
}
