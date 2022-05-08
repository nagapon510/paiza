//9 個の数値が半角スペース区切りで入力されます。
//この数値を 3 行 3 列の形式で出力してください。
//具体的には、入力された数値を N_1 , N_2 , N_3 , ..., N_9 とするとき、 
//1 行目にはN_1 からN_3 を、2 行目には N_4 から N_6 を、3 行目には N_7 から N_9 を出力してください。
//ただし、数値の間には半角スペースを、各行の末尾には、半角スペースの代わりに改行を入れてください。

using System;
using System.Text;
using System.Linq;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        var line = Console.ReadLine();
        var nums = line.Split(' ');
        StringBuilder ret = new StringBuilder();
        Enumerable.Range(0,nums.Length/3).ToList().ForEach(x => ret.Append(String.Join(" ",nums.Skip(x*3).Take(3))).Append("\n"));
        Console.WriteLine(ret);
    }
}