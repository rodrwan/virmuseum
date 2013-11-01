class Place < ActiveRecord::Base
  has_many :items
  attr_accessible :name
end
