//1 から 1,000 までの数値をすべて、半角スペース区切りで出力してください。
//ただし、末尾に半角スペースを出力してはいけません。

using System;

class Program
{
    static void Main()
    {
        string numbers = "";
        for (int i = 1; i <= 1000; i++)
        {
            numbers += i;
            if (i < 1000)
            {
                numbers += " ";
            }
        }
        Console.WriteLine(numbers);
    }
}