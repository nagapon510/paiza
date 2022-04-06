//1 から 1,000 までの数値をすべて、半角スペース区切りで出力してください。
//ただし、末尾に半角スペースを出力してはいけません。

using System;
using System.Text;

class Program
{
    static void Main()
    {
        StringBuilder numbers = new StringBuilder("");
        for (int i = 1; i <= 1000; i++)
        {
            numbers.Append(i);
            if (i < 1000)
            {
                numbers.Append(" ");
            }
        }
        Console.WriteLine(numbers);
    }
}