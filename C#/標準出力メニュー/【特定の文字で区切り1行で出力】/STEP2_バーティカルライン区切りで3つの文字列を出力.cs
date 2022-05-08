//3つの文字列が改行区切りで与えられます。
//これらの文字列をバーティカルライン | 区切りで出力してください。

using System;
using System.Text;
using System.Linq;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        StringBuilder strs = new StringBuilder();
        Enumerable.Range(0,3).ToList().ForEach(x => strs.Append(Console.ReadLine()).Append("|"));
        Console.WriteLine(strs.ToString().Trim('|'));
    }
}