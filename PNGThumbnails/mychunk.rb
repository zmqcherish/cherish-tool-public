  module MYChunk
class Base
 attr_accessor :type
 def initialize(type, attributes = {})
        self.type = type
        attributes.each { |k, v| send("#{k}=", v) }
      end
	  
	  class Generic < Base
	   attr_accessor :content

      def initialize(type, content = '')
        super(type, :content => content)
      end
	  end
end
end