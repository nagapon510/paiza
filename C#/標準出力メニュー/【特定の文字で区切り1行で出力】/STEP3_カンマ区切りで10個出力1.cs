//10 個の数値が半角スペース区切りで与えられます。
//これらの数値すべて受け取り、そのまま出力してください。
//ただし、数値を出力した直後に必ずカンマを、末尾にはさらに改行も出力してください。

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
        Console.WriteLine(ret);
    }
}