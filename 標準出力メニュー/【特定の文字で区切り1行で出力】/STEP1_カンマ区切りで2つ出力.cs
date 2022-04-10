//2 つの数値が半角スペース区切りで与えられます。これらの数値をカンマ区切りで出力してください。

using System;
using System.Linq;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        var line = Console.ReadLine();
        var strs = line.Split(' ');
        Console.WriteLine(strs[0] +"," + strs[1]);
    }
}