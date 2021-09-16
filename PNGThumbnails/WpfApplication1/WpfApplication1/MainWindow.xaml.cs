using System;
using System.Windows;
using System.Drawing;
using System.IO;
using System.Collections.Generic;

namespace WpfApplication1
{
    /// <summary>
    /// MainWindow.xaml 的交互逻辑
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        static string path = @"C:\Users\zmq_c\OneDrive\code\PNGThumbnails\imgs\";
        double gamma = 0.023;
        double fade1 = 220 / 255.0;
        double fade2 = 210 / 255.0;
        double shift = 10;
        Bitmap img1 = (Bitmap)System.Drawing.Image.FromFile(path + "1.png");
        Bitmap img2 = (Bitmap)System.Drawing.Image.FromFile(path + "2.png");

        int trans(byte b)
        {
            double scaled = b * fade1 + shift;
            return (int)Math.Floor(Math.Pow(scaled / 255.0, gamma) * 255.0);
        }
        void createImageFiles()
        {
            Bitmap o = new Bitmap(img1.Size.Width * 2, img1.Size.Height * 2);
            o.MakeTransparent(Color.Black);

            for (int x = 0; x < o.Width; x++)
            {
                for (int y = 0; y < o.Height; y++)
                {
                    if (x % 2 == 0 && y % 2 == 0)
                    {
                        var col = img1.GetPixel(x / 2, y / 2);
                        var r = trans(col.R);
                        var g = trans(col.G);
                        var b = trans(col.B);
                        o.SetPixel(x, y, Color.FromArgb(r, g, b));
                    }
                    else
                    {
                        var col = img2.GetPixel(x / 2, y / 2);
                        var r = Convert.ToInt16(Math.Round(col.R * fade2));
                        var g = Convert.ToInt16(Math.Round(col.G * fade2));
                        var b = Convert.ToInt16(Math.Round(col.B * fade2));
                        o.SetPixel(x, y, Color.FromArgb(r, g, b));
                    }
                }
            }
            //ReadchkType(o);

            SetGAMA(o);
           o.Save(path + "a.png");
        }

        private void button_Click(object sender, RoutedEventArgs e)
        {
            // StripGAMA();

            int pngGamma = (int)(gamma * 100000);

            byte[] bytes = BitConverter.GetBytes(pngGamma);
            // if (BitConverter.IsLittleEndian)
            Array.Reverse(bytes);

            //ReadchkType((Bitmap)System.Drawing.Image.FromFile(path+"3.png"));

            createImageFiles();
            // SetGAMA((Bitmap)System.Drawing.Image.FromFile(path+"a.png"));
        }

        List<xyz> list =new List<xyz>();
        void ReadchkType(Bitmap input)
        {
            MemoryStream ms = new MemoryStream();
            input.Save(ms, System.Drawing.Imaging.ImageFormat.Png);
            byte[] data = ms.ToArray();

            int offset = 8;
            byte[] chkLenBytes = new byte[4];
            int chkLength = 0;
            string chkType = string.Empty;
            while (offset < data.Length - 12)
            {
                chkLenBytes[0] = data[offset];
                chkLenBytes[1] = data[offset + 1];
                chkLenBytes[2] = data[offset + 2];
                chkLenBytes[3] = data[offset + 3];
                if (System.BitConverter.IsLittleEndian)
                    System.Array.Reverse(chkLenBytes);

                chkLength = System.BitConverter.ToInt32(chkLenBytes, 0);


                chkType = System.Text.Encoding.ASCII.GetString(data, offset + 4, 4);
                if (chkType == "gAMA")
                {

                }
                xyz p = new xyz();
                p.len = chkLength;
                p.off = offset;
                p.type = chkType;
                list.Add(p);
                offset += 12 + chkLength;
            }

        }
        public void StripGAMA()
        {
            Bitmap input = (Bitmap)System.Drawing.Image.FromFile(path + "a.png");
            MemoryStream ms = new MemoryStream();
            input.Save(ms, System.Drawing.Imaging.ImageFormat.Png);
            byte[] data = ms.ToArray();

            ms = new MemoryStream();
            ms.Write(data, 0, 8);

            int offset = 8;
            byte[] chkLenBytes = new byte[4];
            int chkLength = 0;
            string chkType = string.Empty;
            while (offset < data.Length - 12)
            {
                chkLenBytes[0] = data[offset];
                chkLenBytes[1] = data[offset + 1];
                chkLenBytes[2] = data[offset + 2];
                chkLenBytes[3] = data[offset + 3];
                if (System.BitConverter.IsLittleEndian)
                    System.Array.Reverse(chkLenBytes);

                chkLength = System.BitConverter.ToInt32(chkLenBytes, 0);


                chkType = System.Text.Encoding.ASCII.GetString(data, offset + 4, 4);
                if (chkType != "gAMA")
                {
                    if (chkType == "IDAT" || chkType == "PLTE")
                    {
                        ms.Write(data, offset, data.Length - offset);
                        break;
                    }
                    else
                    {
                        ms.Write(data, offset, 12 + chkLength);
                        offset += 12 + chkLength;
                    }
                }
                else
                {
                    offset += 12 + chkLength;
                    ms.Write(data, offset, data.Length - offset);
                    break;
                }


            }
            Bitmap bb = new Bitmap(ms);
            bb.Save(path + "o2.png");
        }

        public void SetGAMA(Bitmap input)
        {
            byte[] gammaData = new byte[] { 0, 0, 0, 4, 103, 65, 77, 65, 0, 0, 8, 252, 247, 247, 84, 14 };


            MemoryStream ms = new MemoryStream();
            input.Save(ms, System.Drawing.Imaging.ImageFormat.Png);
            byte[] data = ms.ToArray();

            ms = new MemoryStream();
            ms.Write(data, 0, 8);

            int offset = 8;
            byte[] chkLenBytes = new byte[4];
            int chkLength = 0;
            string chkType = string.Empty;
            while (offset < data.Length - 12)
            {
                chkLenBytes[0] = data[offset];
                chkLenBytes[1] = data[offset + 1];
                chkLenBytes[2] = data[offset + 2];
                chkLenBytes[3] = data[offset + 3];
                if (System.BitConverter.IsLittleEndian)
                    System.Array.Reverse(chkLenBytes);

                chkLength = System.BitConverter.ToInt32(chkLenBytes, 0);


                chkType = System.Text.Encoding.ASCII.GetString(data, offset + 4, 4);

                if (chkType == "gAMA")
                {
                    ms.Write(gammaData, 0, 16);
                    offset += 12 + chkLength;
                    ms.Write(data, offset, data.Length - offset);
                    break;
                }
                else
                {
                    ms.Write(data, offset, 12 + chkLength);
                    offset += 12 + chkLength;
                }
            }
            Bitmap bb = new Bitmap(ms);
            bb.Save(path + "ooo.png");
        }

        public void AddGAMA(Bitmap input)
        {
            byte[] gammaData = new byte[] { 0, 0, 0, 4, 103, 65, 77, 65, 0, 0, 8, 252, 247, 247, 84, 14 };


            MemoryStream ms = new MemoryStream();
            input.Save(ms, System.Drawing.Imaging.ImageFormat.Png);
            byte[] data = ms.ToArray();

            ms = new MemoryStream();
            ms.Write(data, 0, 8);

            int offset = 8;
            byte[] chkLenBytes = new byte[4];
            int chkLength = 0;
            string chkType = string.Empty;
            while (offset < data.Length - 12)
            {
                chkLenBytes[0] = data[offset];
                chkLenBytes[1] = data[offset + 1];
                chkLenBytes[2] = data[offset + 2];
                chkLenBytes[3] = data[offset + 3];
                if (System.BitConverter.IsLittleEndian)
                    System.Array.Reverse(chkLenBytes);

                chkLength = System.BitConverter.ToInt32(chkLenBytes, 0);


                chkType = System.Text.Encoding.ASCII.GetString(data, offset + 4, 4);

                if (chkType == "IHDR")
                {
                    ms.Write(data, offset, 12 + chkLength);
                    offset += 12 + chkLength;
                    ms.Write(gammaData, 0, 16);
                    ms.Write(data, offset, data.Length - offset);
                    break;
                }
            }
            Bitmap bb = new Bitmap(ms);
            bb.Save(path + "o.png");
        }
    }

    class xyz
    {
       public int off { set; get; }
        public int len { set; get; }
        public string type { set; get; }
    }
}
