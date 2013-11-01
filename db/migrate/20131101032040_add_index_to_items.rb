class AddIndexToItems < ActiveRecord::Migration
  def change
  	add_index :items, :id_place
  end
end
