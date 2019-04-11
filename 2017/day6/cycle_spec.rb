require_relative 'cycle'

RSpec.describe Tram::Cycle do
  let(:bank) { [0, 2, 7, 0] }
  let(:instance) { described_class.new(bank) }
  describe ".new" do
    subject { instance }
    it "returns a cycle instance" do
      expect(subject).to be_a Tram::Cycle
    end
  end
  describe ".call" do
    subject { instance.call }
    it "returns the number of redistribution cycles" do
      expect(subject).to eq(5)
    end
  end
end
