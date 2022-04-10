//10 個の数値が半角スペース区切りで与えられます。
//これらの数値をカンマ区切りで出力してください。
//ただし、末尾にはカンマではなく改行を出力してください。

using System;
using System.Text;
using System.Linq;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        StringBuilder ret = new StringBuilder();
        var line = Console.ReadLine();
        var strs = line.Split(' ');
        strs.ToList().ForEach(str => ret.Append(str).Append(','));
        Console.WriteLine(ret.ToString().Trim(','));
    }
}