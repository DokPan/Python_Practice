using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LibraryPython
{

    public class LibraryClass
    {
        public void CreateFile(string path, string text)
        {
            File.WriteAllText(path, text);
            Console.WriteLine("Файл создан: " + path);
        }

        public string ReadFile(string path)
        {
            if (File.Exists(path))
                return File.ReadAllText(path);
            return "Файл не найден";
        }

        public void DeleteFile(string path)
        {
            if (File.Exists(path))
            {
                File.Delete(path);
                Console.WriteLine("Файл удалён: " + path);
            }
        }

        public void AppendFile(string path, string text)
        {
            File.AppendAllText(path, text);
            Console.WriteLine("Текст добавлен в файл: " + path);
        }
    }

}
