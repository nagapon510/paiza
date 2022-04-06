//数値 N が入力されます。1 から N までの数値をすべて、改行区切りで出力してください。

using System;
using System.Linq;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        var number = int.Parse(Console.ReadLine());
        for (int i = 0; i < number; i++)  //条件式の加工を＜に置き換えることで回避
        {
            Console.WriteLine(i + 1);
        }
    }
}