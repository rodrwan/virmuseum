class CreateTermVsItems < ActiveRecord::Migration
  def change
  	create_table :term_vs_items do |t|
      t.integer :count

      t.timestamps
    end
  end
end
