#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>
#include <climits>

using namespace std;

void read_pileup(string input_filename, int* a, int* t, int* c, int* g, long long start, long long end)
{
	ifstream input;
	input.open(input_filename.c_str());

	int i, j;
	int va, vt, vc, vg;
	string chr, content, dummy;
	int locus, copy, num;
	char ref;
	while(input >> chr >> locus >> ref >> copy)
	{
		if(copy == 0) continue;
		input >> content >> dummy;

		if(locus < start || locus >= end) continue;

		va = 0, vt = 0, vc = 0, vg = 0;
		for(i = 0; i < content.size(); i++)
		{
			if(content[i] == '.' || content[i] == ',')
			{
				if(ref == 'A' || ref == 'a') va++;
				else if(ref == 'T' || ref == 't') vt++;
				else if(ref == 'C' || ref == 'c') vc++;
				else if(ref == 'G' || ref == 'g') vg++;
			}
			else if(content[i] == 'A' || content[i] == 'a')
			{
				va++;
			}
			else if(content[i] == 'T' || content[i] == 't')
                        {
                                vt++;
                        }
			else if(content[i] == 'C' || content[i] == 'c')
                        {
                                vc++;
                        }
			else if(content[i] == 'G' || content[i] == 'g')
                        {
                                vg++;
                        }
			else if(content[i] == 'N' || content[i] == 'n')
                        {
                        }
			else if(content[i] == '^')
			{
				i++;
			}
			else if(content[i] == '$')
			{
			}
			else if(content[i] == '*')
			{
			}
			else if(content[i] == '+' || content[i] == '-')
			{
				num = 0;
				for(j = i + 1; j < content.size(); j++)
				{
					if(content[j] >= '0' && content[j] <= '9')
					{
						num = num * 10 + content[j] - '0';
					}
					else
					{
						i = j + num - 1;
						break;
					}
				}
			}
			else
			{
				printf("warning: unknown character %c\n", content[i]);
			}
		}
		a[locus - start + 1] += va;
		t[locus - start + 1] += vt;
		c[locus - start + 1] += vc;
		g[locus - start + 1] += vg;
	}

	input.close();
}

FILE* fileOpenWB(const char* filename)
{
        FILE* file = (FILE*) fopen(filename, "wb");
        if(file == NULL)
        {
                printf("Cannot open the file %s\n", filename);
                exit(1);
        }
        return file;
}

void fileClose(FILE* file)
{
        fclose(file);
}

int main(int argc, char* argv[])
{
	string input_filename = argv[1];
	string output_filename = argv[2];
	string start_locus = argv[3];
	string end_locus = argv[4];
	long long start = atoll(start_locus.c_str());
	long long end = atoll(end_locus.c_str());
	long long genome_len = end - start;

	int* a = (int*) calloc(genome_len + 1, sizeof(int));
	int* t = (int*) calloc(genome_len + 1, sizeof(int));
	int* c = (int*) calloc(genome_len + 1, sizeof(int));
	int* g = (int*) calloc(genome_len + 1, sizeof(int));

	read_pileup(input_filename, a, t, c, g, start, end);

	FILE* output = fileOpenWB(output_filename.c_str());
	int i;
	for(i = 1; i <= genome_len; i++)
	{
		if(a[i] > CHAR_MAX) a[i] = CHAR_MAX;
		if(t[i] > CHAR_MAX) t[i] = CHAR_MAX;
		if(c[i] > CHAR_MAX) c[i] = CHAR_MAX;
		if(g[i] > CHAR_MAX) g[i] = CHAR_MAX;

		fwrite(&a[i], sizeof(char), 1, output);
		fwrite(&t[i], sizeof(char), 1, output);
		fwrite(&c[i], sizeof(char), 1, output);
		fwrite(&g[i], sizeof(char), 1, output);
	}
	fileClose(output);

	return 0;
}

