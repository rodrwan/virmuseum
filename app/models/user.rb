class User < ActiveRecord::Base 
  belongs_to :role
  attr_accessible :name, :role_id
end
