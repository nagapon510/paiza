//10 個の文字列 S_1, S_2, S_3, ..., S_10 が半角スペース区切りで与えられます。
//これらの文字列をすべて、改行区切りで出力してください。

using System;
using System.Linq;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        var line = Console.ReadLine();
        var strs = line.Split(' ');   //Listを配列に変更
        strs.ToList().ForEach(str => Console.WriteLine(str));  //ListでないとForEachが使えないため、ToList()でリストに変換してからForEach
    }
}