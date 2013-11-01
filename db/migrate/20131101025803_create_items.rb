class CreateItems < ActiveRecord::Migration
  def change
    create_table :items do |t|
      t.integer :id_place
      t.integer :visits
      t.string :hierarchy
      t.string :description

      t.timestamps
    end
  end
end
