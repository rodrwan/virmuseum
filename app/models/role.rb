class Role < ActiveRecord::Base
  has_many :data_streams
  attr_accessible :id_user, :kind
end
