ActiveAdmin.register Role do
	index do
        column :id
        column :name
        default_actions
    end
end
