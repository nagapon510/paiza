//1 から 1,000 までの数値をすべて、半角スペース区切りで出力してください。
//ただし、末尾に半角スペースを出力してはいけません。

using System;
using System.Text;
using System.Linq;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        //0-999までの値を+1してリスト化(1-1000) ⇒ リストの値を半角スペースを区切り文字にして連結
        var ret = String.Join(" ", Enumerable.Range(0, 1000).Select(x => x+1).ToList());
        Console.WriteLine(ret);
    }
}