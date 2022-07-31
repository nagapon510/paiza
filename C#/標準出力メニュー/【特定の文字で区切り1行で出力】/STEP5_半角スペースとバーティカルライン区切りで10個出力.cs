//10 個の数値が改行区切りで与えられます。
//これらの数値を半角スペース 2 つとバーティカルライン | 区切りで出力してください。
//ただし、末尾には改行を出力してください。

using System;
using System.Text;
using System.Linq;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        StringBuilder ret = new StringBuilder();
        Enumerable.Range(0,10).ToList().ForEach(x => ret.Append(Console.ReadLine()).Append(" | "));
        int len = ret.Length;
        Console.WriteLine(ret.ToString().Substring(0, len-3));
    }
}