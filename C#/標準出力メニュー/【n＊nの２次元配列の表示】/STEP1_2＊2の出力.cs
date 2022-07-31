//4 つの数値 0, 8, 1, 3 をこの順に、2 行 2 列の形で出力してください。
//ただし、数値の間には半角スペースを、各行の末尾には、半角スペースの代わりに改行を入れてください。

using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        var numbers = new List<int>()
        {
            0, 8, 1, 3
        };
        Console.WriteLine(String.Join(" ",numbers[0],numbers[1]));
        Console.WriteLine(String.Join(" ",numbers[2],numbers[3]));
    }
}