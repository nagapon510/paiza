//数値 N が入力されます。1 から N までの数値をすべて、改行区切りで出力してください。

using System;
using System.Linq;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        var number = int.Parse(Console.ReadLine());
        Enumerable.Range(1, number).ToList().ForEach(x => Console.WriteLine(x)); //1～NまでのリストにしてForEachで出力
    }
}