module Tram
  class Cycle
    def initialize(bank)
      @cycles = [bank]
      @conf_num = cycles.size
      @magic_number = bank.length - 1
    end

    def call
      return cycles.size if cycles.include?(redist_bank)
      
      cycles.push(redist_bank)
      call
    end

    private 

    attr_reader :cycles, :conf_num, :magic_number

    def bank
      cycles.last
    end
    
    def max_with_index
      largest_block = bank.max
      largest_block_index = bank.index(largest_block)
      [largest_block, largest_block_index]
    end

    def redist_bank
      max, max_index = max_with_index
      bank.map.with_index do |element, index|
        if index == max_index
          max % magic_number
        else
          element += max / magic_number
        end
      end
    end
  end
end
