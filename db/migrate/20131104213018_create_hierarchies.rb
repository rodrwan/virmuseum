class CreateHierarchies < ActiveRecord::Migration
  def change
    create_table :hierarchies do |t|
      t.string :name
      t.string :description
      t.integer :parent_id

      t.timestamps
    end
  end
end
