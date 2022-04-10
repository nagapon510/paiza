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
        StringBuilder numbers = new StringBuilder();

        //1～1000の整数をリストにする ⇒ x+1と半角スペースをnumbersに連結 ⇒ Foreachで1000までループ
        Enumerable.Range(0,1000).ToList().ForEach(x => numbers.Append(x+1).Append(" ")); 

        //numbersを文字列に変換してから引数なしのTrimで末尾の空白を削除
        Console.WriteLine(numbers.ToString().Trim());
    }
}