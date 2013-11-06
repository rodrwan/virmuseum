class Role < ActiveRecord::Base
  # has_many :data_streams
  has_one :user
  attr_accessible :name
end
