/**
 *	Name:	Casey Richardson
 *	SID: 	20056054
 *
 *	File: This file is the main point of the interface.
 */

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <string>

using namespace std;

string csubstr(string &input, int begin, int end)
{
	if(end <= input.length())
	{
		char * sub = new char[end - begin];

		for(int j = begin, k = 0; j <= end; j++, k++)
		{
			if(j != end)
				sub[k] = input[j];
			else
				sub[k] = '\0';
		}

		string s(sub);
		return s;
	}
	else
	{
		string s;
		return s;
	}
}

bool cstrcmp(string &input1, string &input2)
{
	if(input1.length() != input2.length())
	{
		return false;
	}
	else
	{
		for (int i = 0; i < input1.length(); i++)
		{
			if(input1[i] != input2[i])
				return false;
		}

		return true;
	}
}

vector<string> tokenizeCommand(string &input)
{
    	// Stores the broken string and is returned at the end.
	vector<string> output;
	int numWords;

    	// Index trackers of the beginning and end of words.
	int beginWord;
	int endWord;
	bool inWord = false;

	for(int i = 0; i <= input.length(); i++)
	{
		char currChar = input[i];

        	// Make sure that we're not currently inside a word.
		if(!inWord)
		{
            		// If the character is not a whitespace character then we start making a new word.
			if(currChar != ' ' || currChar != '\t')
			{
				beginWord = i;
				inWord = true;
			}
		}
		else
		{
            		// Checks if the current character is some form of whitespace.
			if(currChar == ' ' || currChar == '\t' || currChar == '\0')
			{
				endWord = i;
				inWord = false;

				output.push_back(csubstr(input, beginWord, endWord));
			}
		}
	}

	return output;
}

bool isCommand(string &command)
{
	string commands[] = {"maze", "magic", "mazeGame", "movePlayer", "cristallBall", "minheap", "exit"};

	for(int i = 0; i < 7; i++)
	{
		if(cstrcmp(command, commands[i]))
		{
			return true;
		}
	}

	return false;
}

bool commandExists(string &command)
{
	ifstream inputFile((command + ".py").c_str());
	return inputFile;
}

int main(int argc, char **argv)
{
	string input;
	string exitStr("exit");

	system("cls");

	cout << "<======= + + + + HESTEC + + + + =======>" << endl << endl;
	cout << "          HESTEC 2013 Interface         " << endl << endl;
	cout << "<======= + + + + ====== + + + + =======>" << endl;
	cout << "           Copyright© ACM 2013          " << endl << endl;
	while(true)
	{
		cout << "> ";
		getline(cin, input);

		vector<string> command = tokenizeCommand(input);
		if(command.empty())
			continue;
		if(isCommand(command[0]))
		{
			if(cstrcmp(command[0], exitStr))
			{
				break;
			}
			else
			{
				if(commandExists(command[0]))
				{
					system(("python " + command[0] + ".py").c_str());
				}
				else
				{
					cout << "Command \'" << command[0] << "\' is not yet implemented!" << endl;
				}
			}
		}
		else
		{
			cout << "Command not recognized!" << endl;
		}
	}

	return 0;
}