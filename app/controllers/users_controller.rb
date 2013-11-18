class UsersController < InheritedResources::Base
  def index
    @users = User.all

    respond_to do |format|
      format.html # index.html.erb
      format.json { render json: @items }
    end
  end
end
