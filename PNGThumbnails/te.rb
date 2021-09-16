require "chunky_png"
module Te
	def Te.do()
	int = ChunkyPNG::Image.from_file("C:/Users/zmq_c/OneDrive/code/PNGThumbnails/imgs/a.png")
    pngGamma = 2300
    # turn the integer into a 4 byte big-endian unsigned int byte string
    bytestr = [pngGamma].pack("L>") 
    # The chunk is named gAMA because the PNG spec is weird
    chunk = ChunkyPNG::Chunk::Generic.new("gAMA",bytestr)
	out = int.to_datastream
    out.other_chunks << chunk
#out
	 out.save("C:/Users/zmq_c/OneDrive/code/PNGThumbnails/imgs/o1.png")
	end
end