//大きな数値Nが入力されます。
//位の小さい方から 3 けたごとにカンマ区切りで出力してください。
//ただし、Nのけた数は 3 の倍数とは限りません。

//大きな数値 N が入力されます。
//3 けたごとにカンマ区切りで出力してください。
//ただし、N のけた数は 3 の倍数です。

using System;
using System.Text;
using System.Linq;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        var num = Console.ReadLine();
        int len = num.ToString().Length;
        StringBuilder ret = new StringBuilder();
        if (len%3 != 0)
        {
            ret.Append(num.ToString().Substring(0, len%3)).Append(',');
            Enumerable.Range(0,len/3).ToList().ForEach(x => ret.Append(num.ToString().Substring(len%3+x*3, 3)).Append(','));
        } else
        {
            Enumerable.Range(0,len/3).ToList().ForEach(x => ret.Append(num.ToString().Substring(x*3, 3)).Append(','));
        }
        Console.WriteLine(ret.ToString().Trim(','));
    }
}