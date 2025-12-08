css_body = """
/* ---------------- Page Background ---------------- */
	.no-breadcrumbs{
		background: linear-gradient(
			90deg,
			var(--primary),
			var(--secondary)
		) !important;
    }


/* ---------------- NAVBAR ---------------- */
	.navbar {
		background: linear-gradient(
			90deg,
			var(--primary),
			var(--secondary)
		) !important;
	}

	.navbar .awesomplete .form-control {
		border: 1px solid var(--accent) !important;
		border-radius: 6px;
	}

	.navbar .awesomplete .form-control:hover {
		box-shadow: 0 6px 20px rgba(0,0,0,0.1) !important;
	}

	.nav.navbar-nav a {
		color: #000 !important;
		font-weight: 600 !important;
	}
	
/* ---------------- Page Head ---------------- */
	.page-head{
		background: linear-gradient(
			90deg,
			var(--primary),
			var(--secondary)
		) !important;
	}
	
/* ---------------- Page Container ---------------- */
	.page-container{
		background: linear-gradient(
			90deg,
			var(--primary),
			var(--secondary)
		) !important;
	}

/* ---------------- SIDEBAR ---------------- */

	.layout-side-section {
		background: var(--secondary) !important;
  		border-radius: 14px !important;
	}
    
	.workspace-sidebar {
		background: #fff !important;
		border-radius: 6px !important;
		border-right: 1px solid #eee !important;
	}

	.workspace-sidebar .sidebar-item {
		border-radius: 6px !important;
		padding: 10px 14px !important;
		margin-bottom: 6px !important;
		transition: 0.2s ease all;
		font-weight: 600 !important;
	}

	.workspace-sidebar .sidebar-item:hover {
		background: rgba(125, 42, 232, 0.06) !important;
	}

	.workspace-sidebar .sidebar-item.selected {
		background: var(--primary) !important;
		color: #fff !important;
	}

/* ---------------- SIDEBAR SELECTED ---------------- */
	.desk-sidebar-item.standard-sidebar-item.selected {
		background: linear-gradient(
			90deg, 
			var(--secondary), 
			var(--primary)
		) !important;
		font-weight: 700 !important;
	}

/* ---------------- WORKSPACE BODY & TITLE ---------------- */
	.workspace-body {
		background: var(--primary) !important;
		padding-top: 10px;
	}

	.workspace-title .title-text {
		font-size: 26px !important;
		font-weight: 600 !important;
		color: #333 !important;
	}

/* ---------------- WIDGET GRID & CARDS ---------------- */
	.widget-group {
		display: grid !important;
		grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)) !important;
		gap: 18px !important;
	}

	.widget {
		background: var(--secondary) !important;
		border: 1px solid var(--primary) !important;
		border-radius: 6px !important;
		padding: 18px !important;
		box-shadow: 0 4px 14px rgba(0,0,0,0.06) !important;
		transition: 0.25s ease all;
	}

	.widget:hover {
		transform: translateY(-3px);
		box-shadow: 0 6px 20px rgba(0,0,0,0.1) !important;
	}

	.widget.spacer {
		display: none !important;
	}

	/* Widget Titles */
	.widget .widget-head,
	.widget .widget-title .ellipsis {
		font-size: 16px !important;
		font-weight: 600 !important;
		color: var(--primary-text-color-light) !important;
	}

	/* ---------------- SHORTCUT WIDGET ---------------- */
	.shortcut-widget-box {
		background: var(--secondary) !important;
		border-radius: 6px !important;
		padding: 14px !important;
		font-size: 15px !important;
		box-shadow: 0 4px 14px rgba(0,0,0,0.06) !important;
	}

/* ---------------- WIDGET LINKS ---------------- */
	.widget-body a {
		color: #555 !important;
	}

	.widget-body a:hover {
		color: var(--secondary-text-color-light) !important;
	}

	.widget-body .link-item {
		position: relative;
		padding-left: 20px !important;
		display: flex;
		align-items: center;
		margin-bottom: 6px;
	}

	.widget-body .link-item::before {
		content: "•";
		position: absolute;
		left: 0;
		top: 4px;
		font-size: 18px;
		color: var(--secondary-text-color-light);
	}

	.widget-body .link-item:hover::before {
		color: var(--secondary-text-color-light);
	}

/* Buttons */
	.btn-new-workspace,
	.btn-edit-workspace {
		background-color: var(--primary) !important;
		color: var(--primary-text-color-dark) !important;
		font-weight: 600 !important;
		border-radius: 6px !important;
		padding: 6px 14px !important;
		box-shadow: 0 4px 14px rgba(0,0,0,0.06) !important;
		transition: 0.2s ease all;
	}

	.btn-new-workspace:hover,
	.btn-edit-workspace:hover {
		transform: translateY(-3px);
		box-shadow: 0 6px 20px rgba(0,0,0,0.1) !important;
	}
    
    .btn-primary {
		background: var(--primary) !important;
        color: var(--primary-text-color) !important;
    }


/* Standard Filter Section */
	.standard-filter-section .form-control,
	.standard-filter-section input[type="text"] {
		background: #fff !important;
		border: 1px solid #000 !important;
		color: #222 !important;
		border-radius: 7px !important;
		padding: 6px 12px !important;
		transition: 0.2s;
	}

	.standard-filter-section .form-control:focus {
		border-color: var(--primary) !important;
		box-shadow: 0 0 0 2px var(--primary);
	}

	.standard-filter-section .form-group {
		margin-bottom: 12px;
	}

/* List Row Styling */
	.list-row-container {
		border-top: 1px var(--primary) solid !important;
	}

	.list-row-container:nth-of-type(even) {
		background-color: var(--secondary) !important;
		border-top: 1px var(--primary) solid !important;
	}

	.list-row-container:hover .list-row {
		background-color: var(--primary) !important;
		border-top: 1px var(--secondary) solid !important;
	}
	
/* Datatable Rows */
	.datatable .dt-row:not(.dt-row-header):nth-of-type(odd) .dt-cell {
		background-color: var(--secondary) !important;
	}

/* ---------------- EDITOR HEADER ---------------- */
	.ce-header .h4 {
		color: var(--secondary-text-color-light) !important;
	}

/* ---------------- HIDE EXTRA ELEMENTS ---------------- */
	.file-preview div.flex.config-area label.frappe-checkbox {
		display: none !important;
	}

	.comment-wrapper,
	.comment-box {
		display: none !important;
	}



/* ---------------- COMPACT FORM TABS ---------------- */
	.form-page{
		background: var(--secondary) !important;
  		border-radius: 14px !important;
    } 
    
    .form-tabs-list {
		background: var(--secondary) !important;
		border-radius: 12px;
		box-shadow: 0 2px 8px rgba(0,0,0,0.3);
		padding: 2px 4px;
		margin: 5px;
		display: flex;
		justify-content: center;
	}

	.form-tabs-list .nav.form-tabs {
		display: flex;
		border-bottom: none;
		width: 100%;
	}

	.form-tabs-list .nav-link {
		background: var(--secondary) !important;
		border-radius: 4px;
		padding: 8px 18px;
		font-weight: 600;
		font-size: 14px;
		border: none;
		transition: 0.16s;
	}
    
    .new-timeline .activity-title {
		background-color: transparent !important;
    }
    
    .new-timeline .timeline-actions {
		background-color: transparent !important;
    }
    
/* Inputs / Controls */
	.control-input:not(:has(button)) {
		background-color: var(--secondary) !important;
		border-radius: 6px;
		border: 1px solid #ccc;
		transition: 0.2s;
	}
    
	.form-in-grid {
		border-radius: 6px;
		border: 1px solid #ccc;
	}
         
"""
